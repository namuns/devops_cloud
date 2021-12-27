import { useState } from "react";

const pickRandom = () => {
  const ranNumList = [];

  for (let i = 0; i < 7; i++) {
    let num = Math.floor(Math.random() * 44) + 1;

    for (const j in ranNumList) {
      if (num == ranNumList[j]) {
        num = Math.floor(Math.random() * 44 + 1);
      }
    }
    ranNumList.push(num);
  }
  ranNumList.sort(function (a, b) {
    return a - b;
  });

  return ranNumList;
};

function PageLotto() {
  const [numberList, setNumberList] = useState([]);

  const Clicker = () => {
    setNumberList(pickRandom());
  };

  return (
    <>
      <button onClick={Clicker}>번호 추첨하기</button>
      <div>
        <h2>Lotto</h2>
        {numberList.map((PageLotto) => (
          <span
            style={{
              display: "inline-block",
              width: "100px",
              height: "100px",
              borderRadius: "50px",
              textAlign: "center",
              fontSize: "3rem",
              margin: "1rem",
              backgroundColor: "green",
            }}
          >
            {PageLotto}
          </span>
        ))}
      </div>
    </>
  );
}

export default PageLotto;
