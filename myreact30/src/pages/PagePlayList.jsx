import React, { useState } from 'react';
import ReactPlayer from 'react-player';
import videoList from 'data/song_list.json';

function PagePlaylist() {
  const [videoUrl, setVideoUrl] = useState('');
  return (
    <>
      <h2>플레이리스트</h2>
      <ReactPlayer url={videoUrl} />

      {videoList.map((video) => {
        return (
          <div
            onClick={() => {
              setVideoUrl(video.url);
            }}
          >
            <h4>{video.title}</h4>
            <img src={video.thumbnail_url} />
          </div>
        );
      })}
    </>
  );
}

export default PagePlaylist;
