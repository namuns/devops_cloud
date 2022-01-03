import { useState } from "react";

function Counter() {
  const [state, setState] = useState({ value: 0, color: "red" });
  const { value, color } = state;

  const handlePlus = () => {
    setState((prevState) => ({
      ...prevState,
      value: prevState.value + 1,
    }));
  };

  const handleMinus = () => {
    const otherState = (prevState) => {
      return {
        ...prevState,
        value: prevState.value - 1,
      };
    };
    setState(otherState);
  };

  const handleGreen = () => {
    const otherState = (prevState) => {
      return {
        ...prevState,
        color: "green",
      };
    };
    setState(otherState);
  };

  const handleBlue = () => {
    const otherState = (prevState) => {
      return {
        ...prevState,
        color: "blue",
      };
    };
    setState(otherState);
  };

  const handleRed = () => {
    const otherState = (prevState) => {
      return {
        ...prevState,
        color: "red",
      };
    };
    setState(otherState);
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
