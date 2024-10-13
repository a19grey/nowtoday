"use client";

import React, { createContext, useEffect, useState } from "react";
import { User } from "firebase/auth";
import { auth, signInWithGoogle as firebaseSignInWithGoogle } from "@/lib/firebase/firebase";

interface AuthContextType {
  user: User | null;
  signInWithGoogle: () => Promise<void>;
  signOut: () => Promise<void>;
}

export const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => {
    const unsubscribe = auth.onAuthStateChanged((user) => {
      setUser(user);
    });

    return () => unsubscribe();
  }, []);

  const signInWithGoogle = async () => {
    console.log("signInWithGoogle called in AuthContext");
    try {
      await firebaseSignInWithGoogle();
      console.log("Firebase signInWithGoogle completed");
    } catch (error) {
      console.error("Error in signInWithGoogle:", error);
      throw error;
    }
  };

  const signOut = async () => {
    try {
      await auth.signOut();
      console.log("User signed out successfully");
    } catch (error) {
      console.error("Error signing out:", error);
      throw error;
    }
  };

  return (
    <AuthContext.Provider value={{ user, signInWithGoogle, signOut }}>
      {children}
    </AuthContext.Provider>
  );
};
