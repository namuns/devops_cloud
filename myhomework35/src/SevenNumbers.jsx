import { useReducer } from 'react';

const range = (size) => [...Array(size).keys()];

function reducer(state, action) {
  switch (action.type) {
    case 'GENERATE_NUMBERS':
      return { ...state, numbers: randomNumbers() };
    case 'SHUFFLE_NUMBERS':
      return {
        ...state,
        numbers: state.numbers.sort(() => Math.random() - Math.random()),
      };
    case 'SHUFFLE_COLORS':
      return {
        ...state,
        colors: state.colors.sort(() => Math.random() - Math.random()),
      };
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
    colors: [
      '#1B62BF',
      '#1755A6',
      '#37A647',
      '#F29F05',
      '#F23838',
      'purple',
      'pink',
    ],
  });

  const generateNumbers = () => {
    dispatch({ type: 'GENERATE_NUMBERS' });
  };

  const shuffleNumbers = () => {
    dispatch({ type: 'SHUFFLE_NUMBERS' });
  };

  const shuffleColors = () => {
    dispatch({ type: 'SHUFFLE_COLORS' });
  };

  return (
    <div>
      <h2>Number7</h2>
      <div>
        <button onClick={generateNumbers}>GENERATE_NUMBERS</button>
        <button onClick={shuffleNumbers}>SHUFFLE_NUMBERS</button>
        <button onClick={shuffleColors}>SHUFFLE_COLORS</button>
        <br />
        {state.numbers.map((num, index) => {
          return (
            <div
              style={{ ...defaultStyle, backgroundColor: state.colors[index] }}
            >
              {num}
            </div>
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
