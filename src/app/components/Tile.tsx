import { useEffect, useState } from "react";
import { Share2, MoreVertical, Download } from 'lucide-react';

interface TileProps {
  id: string;
  title: string;
  width: number;
  height: number;
  color: string;
  partyMode: boolean;
  onShare: (id: string) => void;
  onDownload: (id: string) => void;
}

interface TileContent {
  content: string;
  chartData: string;
}

export default function Tile({ id, title, width, height, color, partyMode, onShare, onDownload }: TileProps) {
  const [tileContent, setTileContent] = useState<TileContent | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(`/api/tiles/${id}`);
        const data = await response.json();
        setTileContent(data);
      } catch (error) {
        console.error("Error fetching tile data:", error);
      }
    };
    fetchData();
  }, [id]);

  return (
    <div
      className={`
        bg-gradient-to-br from-white via-gray-50 to-gray-100
        rounded-xl
        p-3 flex flex-col justify-between
        col-span-${width} row-span-${height}
        transition-all duration-300 ease-in-out
        group
      `}
      style={{
        boxShadow: partyMode 
          ? `0 4px 6px ${color}40, inset 0 -2px 4px ${color}20, inset 0 2px 4px ${color}20` 
          : '0 2px 3px rgba(0,0,0,0.03), inset 0 -1px 2px rgba(0,0,0,0.02), inset 0 1px 2px rgba(255,255,255,0.03)'
      }}
    >
      <div className="flex justify-between items-start">
        <h2 className="text-base font-semibold text-gray-800 group-hover:text-gray-900 transition-colors duration-300">{title}</h2>
        <div className="flex space-x-1">
          <button
            onClick={() => onShare(id)}
            className="text-gray-400 hover:text-gray-600 transition-colors duration-200 relative"
            aria-label={`Share ${title}`}
          >
            <Share2 className="w-3.5 h-3.5" />
            <span className="absolute inset-0 bg-gray-200 opacity-0 group-hover:animate-ping rounded-full" />
          </button>
          <div className="relative group/menu">
            <button 
              className="text-gray-400 hover:text-gray-600 transition-colors duration-200"
              aria-label={`More options for ${title}`}
            >
              <MoreVertical className="w-3.5 h-3.5" />
            </button>
            <div className="absolute right-0 mt-2 w-36 bg-white rounded-md shadow-lg opacity-0 invisible group-hover/menu:opacity-100 group-hover/menu:visible transition-all duration-200 ease-in-out z-10">
              <button
                onClick={() => onDownload(id)}
                className="flex items-center px-2 py-1.5 text-xs text-gray-700 hover:bg-gray-100 w-full text-left rounded-md transition-colors duration-150"
              >
                <Download className="w-3 h-3 mr-1.5" />
                Download Data
              </button>
            </div>
          </div>
        </div>
      </div>
      {tileContent ? (
        <div className="mt-2">
          <p className="text-xs text-gray-600 group-hover:text-gray-700 transition-colors duration-300">{tileContent.content}</p>
          <div className="bg-gray-100 p-2 rounded mt-2">
            <p className="text-sm font-bold">{tileContent.chartData}</p>
          </div>
        </div>
      ) : (
        <p className="mt-2 text-xs text-gray-500">Loading...</p>
      )}
    </div>
  );
}