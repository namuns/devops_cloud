import { useReducer } from "react";

function reducer(prevState, action) {
  const { type, amount, color } = action;
  if (type === "COUNT") {
    return { ...prevState, value: prevState.value + amount };
  } else if (type === "CHANGE_COLOR") {
    return { ...prevState, color: color };
  }
  return prevState;
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, { value: 0, color: "red" });
  const { value, color } = state;

  const handlePlus = () => {
    // const action = { type: "COUNT", amount: 1 };
    dispatch({ type: "COUNT", amount: 1 });
  };

  const handleMinus = () => {
    // const action = { type: "COUNT", amount: -1 };
    // setState((prevState) => {
    //   return reducer(action, prevState);
    // });
    dispatch({ type: "COUNT", amount: -1 });
  };

  const handleGreen = () => {
    // const action = { type: "CHANGE_COLOR", color: "green" };
    // setState((prevState) => {
    //   return reducer(action, prevState);
    // });
    dispatch({ type: "CHANGE_COLOR", color: "green" });
  };

  const handleBlue = () => {
    // const action = { type: "CHANGE_COLOR", color: "blue" };
    // setState((prevState) => {
    //   return reducer(action, prevState);
    // });
    dispatch({ type: "CHANGE_COLOR", color: "blue" });
  };

  const handleRed = () => {
    // const action = { type: "CHANGE_COLOR", color: "red" };
    // setState((prevState) => {
    //   return reducer(action, prevState);
    // });
    dispatch({ type: "CHANGE_COLOR", color: "red" });
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
