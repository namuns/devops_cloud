import { useReducer } from 'react';

const range = (size) => [...Array(size).keys()];

function reducer(state, action) {
  switch (action.type) {
    case 'GENERATE_NUMBERS':
      return { ...state, numbers: randomNumbers() };
    default:
      return state;
  }
}

function randomNumbers() {
  const random_numbers = range(45)
    .sort(() => Math.random() - Math.random())
    .map((number) => number + 1)
    .slice(0, 7);
  return random_numbers;
}

function SevenNumbers() {
  const [state, dispatch] = useReducer(reducer, {
    numbers: [0, 0, 0, 0, 0, 0, 0],
    colors: ['pink'],
  });

  const generateNumbers = () => {
    dispatch({ type: 'GENERATE_NUMBERS' });
  };

  return (
    <div>
      <h2>Number7</h2>
      <div>
        <button onClick={generateNumbers}>GENERATE_NUMBERS</button>
        <br />
        {state.numbers.map((num) => {
          return (
            <div style={{ ...defaultStyle, backgroundColor: 'red' }}>{num}</div>
          );
        })}
      </div>

      <hr />
      {JSON.stringify(state)}
    </div>
  );
}

const defaultStyle = {
  width: '100px',
  height: '100px',
  borderRadius: '100px',
  lineHeight: '100px',
  textAlign: 'center',
  display: 'inline-block',
  fontSize: '3rem',
  userSelect: 'none',
};
export default SevenNumbers;
