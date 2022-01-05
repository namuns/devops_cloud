import './Review.css';
import heart from './heart';

function Review({ review }) {
  const heart = Array(5).fill(0);
  return (
    <div
      className={`m-1 p-1 rounded-lg text-lg border-blue-200 border-2 hover:border-blue-500 hover:scale-105 cursor-pointer`}
    >
      {heart.map((_, index) => {
        return <heart key={index} />;
      })}

      {review.content}
    </div>
  );
}

export default Review;
