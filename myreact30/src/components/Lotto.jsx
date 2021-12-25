import { useState } from 'react';
import Ball from './Ball';

function LottoNumber() {
  const [NumberList, setNumberList] = useState([]);
  const randomInt = () => {
    let RanNumList = [];

    for (let i = 0; i < 7; i++) {
      let num = Math.floor(Math.random() * 44) + 1;

      for (const j in RanNumList) {
        if (num == RanNumList[j]) {
          num = Math.floor(Math.random() * 44) + 1;
        }
      }
      RanNumList.push(num);
    }
    RanNumList.sort(function (a, b) {
      return a - b;
    });

    return RanNumList;
  };

  const handleClick = () => {
    setNumberList(randomInt);
  };
  return (
    <>
      <button onClick={handleClick}>번호 점지하기</button>
      <hr />
      {NumberList.map((number) => (
        <Ball number={number} />
      ))}
    </>
  );

  //  <div style={{ ...style, backgroundColor: color }}>{lotto}</div>;
}

export default LottoNumber;
