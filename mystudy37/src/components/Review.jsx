import './Review.css';

function Review({ review, onClick }) {
  return (
    <div
      className={`m-1 p-1 rounded-lg text-lg border-blue-200 border-2 hover:border-blue-500 hover:scale-105 cursor-pointer text-white`}
      style={{ backgroundColor: review.color }}
    >
      {review.color}
      {review.content}
    </div>
  );
}

export default Review;
