import { useState } from 'react';
import Review from './Review';
import ReviewForm from './ReviewForm';
import './ReviewList.css';
import useFieldValues from 'hooks/useFieldValues';

const INITIAL_STATE = [
  { content: '장고 업글하기' },
  { content: '파이썬 업글하기' },
  { content: '리액트 업글하기' },
];

function ReviewList() {
  const [reviewList, setReviewList] = useState(INITIAL_STATE);
  const [fieldValues, handleChange] = useFieldValues();

  const removeReview = (reviewIndex) => {
    setReviewList((prevReviewList) =>
      prevReviewList.filter((_, index) => index !== reviewIndex),
    );
  };

  return (
    <div className="review-List">
      <h2 className="text-3xl font-bold underline">Review List</h2>

      <ReviewForm handleChange={handleChange} />
      <hr />
      {JSON.stringify(fieldValues)}

      {reviewList.map((review, index) => (
        <Review review={review} onClick={() => removeReview(index)} />
      ))}
    </div>
  );
}

export default ReviewList;
