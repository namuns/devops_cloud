import { useState } from 'react';
import { Button } from 'react-bootstrap';
import initialSongList from 'data/melon_data.json';
import 'MelonTop100.css';

function MelonTop100() {
  const [songList, setSongList] = useState([]);
  const handleClick = () => {
    setSongList(initialSongList);
  };

  return (
    <div>
      <h2>멜론 top 100</h2>
      <Button onClick={handleClick}>로딩</Button>
      <ul className="songList">
        {songList.map((song) => {
          return (
            <li>
              {song.rank} {song.title} by {song.artist} {song.like}
            </li>
          );
        })}
      </ul>
    </div>
  );
}

export default MelonTop100;
