import { useState } from 'react';
import Review from './Review';
import ReviewForm from './ReviewForm';
import './ReviewList.css';
import useFieldValues from 'hooks/useFieldValues';

const INITIAL_STATE = [
  { content: '기본 리뷰 1', heart: 5 },
  { content: '기본 리뷰 2', heart: 4 },
  { content: '기본 리뷰 3', heart: 3 },
];

const INITIAL_VALUE = {
  content: '',
  heart: 0,
};

function ReviewList() {
  const [reviewList, setReviewList] = useState(INITIAL_STATE);
  const [showForm, setShowFrom] = useState();
  const [fieldValues, handleChange, clearFieldValues] =
    useFieldValues(INITIAL_VALUE);

  const removeReview = (reviewIndex) => {
    setReviewList((prevReviewList) =>
      prevReviewList.filter((_, index) => index !== reviewIndex),
    );
  };

  const appendReview = () => {
    console.log('새로운 review추가');
    setReviewList((prevReviewList) => [...prevReviewList, { ...fieldValues }]);
    setShowFrom((prevState) => !prevState);
    clearFieldValues();
  };
  return (
    <div className="review-list">
      <h2 className="text-3xl font-bold underline">Review List</h2>

      {showForm && (
        <ReviewForm
          handleSubmit={appendReview}
          handleChange={handleChange}
        ></ReviewForm>
      )}

      <hr />
      {JSON.stringify(fieldValues)}
      <button
        className="bg-orange-200 hover:bg-orange-400 p-1 rounded text-sm"
        onClick={() => setShowFrom((prevState) => !prevState)}
      >
        New Review
      </button>

      {reviewList.map((review, index) => (
        <Review review={review} onClick={() => removeReview(index)} />
      ))}
    </div>
  );
}

export default ReviewList;
