import { useState } from "react";

// { type: "PLUS", amount: 1 }
// { type: "MINUS", amount: 1 }
function dispatch(action, prevState) {
  const { type, amount } = action;
  if (type === "PLUS") {
    return prevState + amount;
  } else if (type === "MINUS") {
    return prevState - amount;
  }
  // 버그 !!!
  return prevState;
}

function Counter2() {
  // TODO: color와 value
  const [value, setValue] = useState(0);

  const handlePlus = () => {
    const action = { type: "PLUS", amount: 1 };
    setValue((prevValue) => {
      // dispatch 함수를 호출하여, 새로운 상탯값을 계산해냅니다.
      return dispatch(action, prevValue);
    });
  };

  const handleMinus = () => {
    const action = { type: "MINUS", amount: 1 };
    setValue((prevValue) => {
      return dispatch(action, prevValue);
    });
  };

  return (
    <div>
      <h2>Counter2</h2>
      {value}
      <hr />
      <button onClick={handlePlus}>증가</button>
      <button onClick={handleMinus}>감소</button>
    </div>
  );
}

export default Counter2;

// 1. 새로운 상탯값 color, setColor을 정의
//  - 초기값 : "red"
// 2. 3개의 버튼 "색상 변경"
//  - 1번 버튼 클릭하면 : green => { action: "CHANGE_COLOR", color: "green"}
//  - 2번 버튼 클릭하면 : blue => { action: "CHANGE_COLOR", color: "blue"}
//  - 3번 버튼 클릭하면 : red => { action: "CHANGE_COLOR", color: "red"}
// 3. 새로운 dispatch 함수인 dispatch_color를 구현

// function dispatch(action, state) {
//     const { type, payload } = action;
//     if (type === "INCREMENT") {
//       const { value } = payload;
//       return {
//         ...state,
//         value: state.value + value,
//       };
//     } else {
//       return state;
//     }
//   }

//   const action = { type: "INCREMENT", payload: { value: 1 } };
//   dispatch(action);

//   dispatch({
//     type: "INCREMENT",
//     payload: { value: 3 },
//   });
