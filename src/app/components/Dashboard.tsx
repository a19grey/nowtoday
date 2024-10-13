"use client";

import { useState, useEffect, FormEvent } from 'react'
import { Input } from "@/app/components/ui/input"
import { Card } from "@/app/components/ui/card"
import { Globe, Play } from "lucide-react"
import Link from 'next/link'
import { useAuth } from '@/lib/hooks/useAuth'; // If keeping authentication
import ReactPlayer from 'react-player' // For video playback

const BACKEND_URL = 'http://localhost:5002';
const FRONTEND_URL = 'http://localhost:3000';

export default function Dashboard() {
  console.log('Dashboard component rendering');
  console.log('BACKEND_URL:', BACKEND_URL);

  const { user, signOut } = useAuth(); // If keeping authentication
  const [url, setUrl] = useState("")
  const [videoUrl, setVideoUrl] = useState("")
  const [status, setStatus] = useState("Ready to generate your daily summary...")
  const [progress, setProgress] = useState(0)
  const [response, setResponse] = useState("")

  const generateVideo = async () => {
    setStatus("Generating video...")
    try {
      const response = await fetch('/api/generate-video', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url })
      })
      const data = await response.json()
      setVideoUrl(data.videoUrl)
      setStatus("Video generated successfully!")
    } catch (error) {
      setStatus("Error generating video. Please try again.")
    }
  }

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    console.log('handleSubmit function called');
    e.preventDefault()
    setStatus("Sending request...")
    try {
      const fullUrl = `${BACKEND_URL}/api/generate`
      console.log('Sending request to:', fullUrl)
      console.log('Request body:', JSON.stringify({ url }))
      const response = await fetch(fullUrl, {
        method: 'POST',
        headers: { 
          'Content-Type': 'application/json',
          'Accept': 'application/json',
        },
        mode: 'cors',
        credentials: 'omit',
        body: JSON.stringify({ url })
      })
      console.log('Response status:', response.status)
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json()
      console.log('Received response:', data)
      setResponse(data.message)
      setStatus("Response received!")
    } catch (error) {
      console.error('Error:', error);
      setStatus(`Error connecting to backend: ${error instanceof Error ? error.message : 'Unknown error'}`);
    }
  }

  useEffect(() => {
    const timer = setInterval(() => {
      setProgress((oldProgress) => {
        const newProgress = Math.min(oldProgress + 1, 100)
        if (newProgress === 100) {
          clearInterval(timer)
        }
        return newProgress
      })
    }, 100)

    return () => clearInterval(timer)
  }, [])

  return (
    <div className="min-h-screen bg-gray-100 p-8 relative overflow-hidden">
      <div className="absolute inset-0 opacity-5">
        <div className="absolute inset-0 bg-gradient-to-r from-orange-500 to-gray-500" style={{backgroundImage: "url(\"data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23000000' fill-opacity='0.1'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E\")"}}></div>
      </div>
      
      <div className="relative">
        <header className="mb-8 text-center">
          <h1 className="text-6xl font-mono font-bold inline-block mb-4">
            <span className="text-orange-500">NOW</span>
            <span className="text-gray-500">TODAY</span>
          </h1>
          <p className="text-gray-700 text-xl max-w-2xl mx-auto">
            Daily create a summary video from any website and get it in your inbox or push to socials
          </p>
        </header>
        <div className="max-w-2xl mx-auto space-y-8">
          <form onSubmit={handleSubmit}>
            <div className="relative">
              <Input 
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                type="text" 
                placeholder="Enter website URL (e.g., https://news.ycombinator.com)"
                className="w-full shadow-md pl-10 pr-4 py-3 transition-all duration-300 ease-in-out hover:shadow-lg focus:ring-2 focus:ring-orange-500"
              />
              <Globe className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" size={20} />
            </div>
            <button type="submit" className="mt-4 bg-orange-500 text-white px-4 py-2 rounded hover:bg-orange-600 transition-colors">
              Submit
            </button>
          </form>
          {response && (
            <Card className="p-6 shadow-md bg-white">
              <p className="text-sm text-gray-600">{response}</p>
            </Card>
          )}
          <Card className="aspect-video bg-gradient-to-br from-gray-200 to-gray-300 flex items-center justify-center text-gray-500 overflow-hidden group">
            <div className="relative">
              <Play size={48} className="text-gray-400 group-hover:text-orange-500 transition-colors duration-300" />
              <div className="absolute inset-0 bg-orange-500 rounded-full animate-ping opacity-75"></div>
            </div>
            <p className="mt-4 font-medium">Video output will appear here</p>
          </Card>
          <Card className="p-6 shadow-md bg-white">
            <p className="text-sm text-gray-600 mb-4">{status}</p>
            <div className="relative pt-1">
              <div className="overflow-hidden h-24 w-24 mx-auto rounded-full bg-gray-200 shadow-inner">
                <div 
                  className="h-full w-full bg-gradient-to-t from-orange-400 to-orange-600 rounded-full relative"
                  style={{
                    transform: `translateY(${100 - progress}%)`,
                    transition: 'transform 0.5s ease-out'
                  }}
                >
                  <div className="absolute inset-0 bg-white opacity-25 animate-pulse"></div>
                </div>
              </div>
            </div>
          </Card>
          <button onClick={generateVideo}>Generate Video</button>
          {videoUrl && (
            <ReactPlayer url={videoUrl} controls />
          )}
        </div>
        <div className="mt-16 text-center">
          <blockquote className="italic text-gray-700 max-w-2xl mx-auto">
            "Woah... this is more powerful than the atom bomb... for generating video content on socials. It is objectively not as powerful as fission."
            <footer className="text-gray-500 mt-2">- J. Robert Oppenheimer</footer>
          </blockquote>
        </div>
        <footer className="mt-16 text-center text-sm text-gray-500">
          <div className="mb-4">
            <Link href="#" className="text-gray-600 hover:text-orange-500 mx-2">Home</Link>
            <Link href="#" className="text-gray-600 hover:text-orange-500 mx-2">About</Link>
            <Link href="#" className="text-gray-600 hover:text-orange-500 mx-2">Contact</Link>
            <Link href="#" className="text-gray-600 hover:text-orange-500 mx-2">Privacy Policy</Link>
          </div>
          <p>Powered by Grey Labs AI Technology</p>
          <p className="mt-2">© 2023 Grey Labs. All rights reserved.</p>
        </footer>
      </div>
    </div>
  )
}