"use client";

import { Share2, MoreVertical, Download, LogOut } from 'lucide-react'
import { useState, useCallback, useEffect } from 'react'
import { useAuth } from '@/lib/hooks/useAuth';
import SignInWithGoogle from './SignInWithGoogle';
import Tile from './Tile';

interface TileData {
  id: string
  title: string
  width: number
  height: number
  color: string
}

export default function SuperDashboard() {
  const { user, signOut } = useAuth();
  const [loading, setLoading] = useState(true);
  const [isAuthorized, setIsAuthorized] = useState(false);

  const [tiles] = useState<TileData[]>([
    { id: 'tile1', title: 'Tile 1', width: 2, height: 4, color: '#ff6b6b' },
    { id: 'tile2', title: 'Tile 2', width: 1, height: 1, color: '#4ecdc4' },
    { id: 'tile3', title: 'Tile 3', width: 1, height: 1, color: '#45b7d1' },
    { id: 'tile4', title: 'Tile 4', width: 2, height: 2, color: '#f7b731' }
  ])

  const [partyMode, setPartyMode] = useState(false)

  const handleShare = (id: string) => {
    console.log(`Sharing tile ${id}`)
  }

  const handleDownload = (id: string) => {
    console.log(`Downloading data for tile ${id}`)
  }

  const togglePartyMode = useCallback(() => {
    setPartyMode(prev => !prev)
  }, [])

  const handleLogout = async () => {
    try {
      await signOut();
      console.log("User logged out successfully");
    } catch (error) {
      console.error("Error logging out:", error);
    }
  };

  useEffect(() => {
    const checkUserDomain = async () => {
      if (user) {
        const email = user.email;
        if (email && (email.endsWith('@traceup.com') || email.endsWith('@tracevision.com'))) {
          setIsAuthorized(true);
        } else {
          console.log("Unauthorized email domain detected. Signing out...");
          await signOut();
          setIsAuthorized(false);
        }
      } else {
        setIsAuthorized(false);
      }
      setLoading(false);
    };

    checkUserDomain();
  }, [user, signOut]);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (!user || !isAuthorized) {
    return <SignInWithGoogle />;
  }

  return (
    <div className="min-h-screen bg-gray-100 p-4 font-mono relative overflow-hidden">
      <div className="absolute inset-0 bg-gradient-to-br from-gray-100 to-gray-200 opacity-50" style={{
        backgroundImage: "url(\"data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%239C92AC' fill-opacity='0.05'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E\")"
      }} />
      <div className="relative z-10">
        <div className="flex justify-between items-center mb-4">
          <h1 className="text-4xl font-bold text-gray-800">
            SuperDashboard
            <span 
              className="cursor-pointer" 
              onClick={togglePartyMode}
              aria-hidden="true"
            >.</span>
          </h1>
          <button
            onClick={handleLogout}
            className="text-gray-600 hover:text-gray-800 transition-colors duration-200"
            aria-label="Logout"
          >
            <LogOut className="w-6 h-6" />
          </button>
        </div>
        <div className="grid grid-cols-4 gap-[1.8px]">
          {tiles.map((tile) => (
            <Tile
              key={tile.id}
              id={tile.id}
              title={tile.title}
              width={tile.width}
              height={tile.height}
              color={tile.color}
              partyMode={partyMode}
              onShare={handleShare}
              onDownload={handleDownload}
            />
          ))}
        </div>
      </div>
    </div>
  )
}