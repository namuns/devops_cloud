import { useState } from "react";

function reducer(action, prevState) {
  const { type, amount, color } = action;
  if (type === "COUNT") {
    return { ...prevState, value: prevState.value + amount };
  } else if (type === "CHANGE_COLOR") {
    return { ...prevState, color: color };
  }
  return prevState;
}

function Counter() {
  const [state, setState] = useState({ value: 0, color: "red" });
  const { value, color } = state;

  const handlePlus = () => {
    const action = { type: "COUNT", amount: 1 };
    setState((prevState) => {
      return reducer(action, prevState);
    });
  };

  const handleMinus = () => {
    const action = { type: "COUNT", amount: -1 };
    setState((prevState) => {
      return reducer(action, prevState);
    });
  };

  const handleGreen = () => {
    const action = { type: "CHANGE_COLOR", color: "green" };
    setState((prevState) => {
      return reducer(action, prevState);
    });
  };

  const handleBlue = () => {
    const action = { type: "CHANGE_COLOR", color: "blue" };
    setState((prevState) => {
      return reducer(action, prevState);
    });
  };

  const handleRed = () => {
    const action = { type: "CHANGE_COLOR", color: "red" };
    setState((prevState) => {
      return reducer(action, prevState);
    });
  };

  return (
    <div>
      <h2>Counter</h2>
      <div style={{ ...defaultStyle, backgroundColor: color }}>{value}</div>
      <h3>
        <button onClick={handlePlus}>+</button>
        <button onClick={handleMinus}>-</button>
        <button onClick={handleGreen}>green</button>
        <button onClick={handleBlue}>blue</button>
        <button onClick={handleRed}>red</button>
      </h3>
    </div>
  );
}

const defaultStyle = {
  width: "100px",
  height: "100px",
  borderRadius: "50px",
  lineHeight: "100px",
  textAlign: "center",
  display: "inline-block",
  fontSize: "3rem",
  userSelect: "none",
};

export default Counter;
