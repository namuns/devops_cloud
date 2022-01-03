import { useReducer } from 'react';

function reducer(prevState, action) {
  const { type, color } = action;
  if (type === 'generateNumbers') {
    let numList = [];
    for (let i = 1; i < 46; i++) {
      numList.push(i);
    }
    const shuffledNumber = numList
      .map((num_random) => ({
        num_random,
        value: Math.random(),
      }))
      .sort((obj_a, obj_b) => {
        return obj_a.value - obj_b.value;
      })
      .map(({ num_random }) => {
        return num_random;
      })
      .slice(0, 7);
    return { number: shuffledNumber };
  } else if (type === 'COLOR') {
    return { prevState, color };
  }
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
    dispatch({ type: 'generateNumbers' });
  };

  return (
    <div>
      <h2>Number7</h2>
      <div>
        <button onClick={generateNumbers}>GENERATE_NUMBERS</button>
        <br />
        {state.number &&
          state.number.map((num) => {
            return (
              <div style={{ ...defaultStyle, backgroundColor: 'red' }}>
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
