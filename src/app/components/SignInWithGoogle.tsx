"use client";

import { useAuth } from "@/lib/hooks/useAuth";
import { FcGoogle } from "react-icons/fc";
import { signInWithPopup, GoogleAuthProvider } from "firebase/auth";
import { auth } from "@/lib/firebase/firebase";

export default function SignIn() {
  const { signInWithGoogle } = useAuth();

  const handleSignIn = async () => {
    console.log("Sign-in button clicked");
    try {
      console.log("Attempting to sign in with Google...");
      const provider = new GoogleAuthProvider();
      provider.setCustomParameters({
        hd: "gmail.com", // This sets the hosted domain parameter
      });

      const result = await signInWithPopup(auth, provider);
      const user = result.user;

      // Check if the user's email domain is allowed
      if (
        user.email?.endsWith("@gmail.com") ||
        user.email?.endsWith("@tracevision.com")
      ) {
        console.log("Sign-in successful");
      } else {
        // Sign out the user if the domain is not allowed
        await auth.signOut();
        throw new Error("Unauthorized email domain");
      }
    } catch (error) {
      console.error("Error signing in:", error);
      alert("Sign-in failed. Please use an authorized email domain.");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-8 rounded-lg shadow-md">
        <h1 className="text-2xl font-bold mb-4 text-center">
          Welcome to SuperDashboard
        </h1>
        <button
          onClick={handleSignIn}
          className="w-full flex items-center justify-center bg-white border border-gray-300 rounded-lg shadow-md px-6 py-2 text-sm font-medium text-gray-800 hover:bg-gray-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500"
        >
          <FcGoogle className="w-6 h-6 mr-2" />
          Sign in with Google
        </button>
      </div>
    </div>
  );
}
