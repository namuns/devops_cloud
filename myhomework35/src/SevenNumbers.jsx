import { useReducer } from 'react';

function reducer(prevState, action) {}
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
  return (
    <div>
      <h2>Number7</h2>
      <hr />
    </div>
  );
}

export default SevenNumbers;
