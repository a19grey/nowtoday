import { NextResponse } from "next/server";
import { spawn } from "child_process";
import { doc, getDoc } from "firebase/firestore";
import { db } from "@/lib/firebase/firebase";

export async function GET(
  request: Request,
  { params }: { params: { id: string } }
) {
  const { id } = params;

  // Fetch the SQL query associated with the tile from Firebase Firestore
  const docRef = doc(db, "tiles", id);
  const docSnap = await getDoc(docRef);

  if (!docSnap.exists()) {
    return NextResponse.json({ error: "Tile not found" }, { status: 404 });
  }

  const sqlQuery = docSnap.data().sqlQuery;

  // Call a Python script to execute the query and generate the chart
  return new Promise((resolve) => {
    const pythonProcess = spawn("python3", [
      "./scripts/generate_chart.py",
      sqlQuery,
    ]);

    let imageData = "";

    pythonProcess.stdout.on("data", (data) => {
      imageData += data.toString();
    });

    pythonProcess.on("close", () => {
      resolve(NextResponse.json({ data: { imageUrl: imageData } }));
    });
  });
}