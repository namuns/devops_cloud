import { useState } from 'react';
import Review from './Review';
import ReviewForm from './ReviewForm';
import './ReviewList.css';
import useFieldValues from 'hooks/useFieldValues';

const INITIAL_STATE = [
  { content: '장고 업글하기', color: 'coral' },
  { content: '파이썬 업글하기', color: 'coral' },
  { content: '리액트 업글하기', color: 'coral' },
];

function ReviewList() {
  const [reviewList, setReviewList] = useState(INITIAL_STATE);
  const [fieldValues, handleChange, clearFieldValues] = useFieldValues({
    content: '',
    color: 'red',
  });
  const removeReview = (reviewIndex) => {
    setReviewList((prevReviewList) =>
      prevReviewList.filter((_, index) => index !== reviewIndex),
    );
  };

  const appendReview = () => {
    console.log('새로운 review추가');

    const review = { ...fieldValues };

    //setter에 값 함수 지정 방식

    setReviewList((prevReviewList) => [...prevReviewList, review]);

    clearFieldValues();
  };
  return (
    <div className="review-List">
      <h2 className="text-3xl font-bold underline">Review List</h2>
      <ReviewForm
        fieldValues={fieldValues}
        handleChange={handleChange}
        handleSubmit={appendReview}
      />

      <hr />
      {JSON.stringify(fieldValues)}
      <button
        className="bg-red-500 text-gray-100 cursor-pointer"
        onClick={() => clearFieldValues()}
      >
        clear
      </button>

      {reviewList.map((review, index) => (
        <Review review={review} onClick={() => removeReview(index)} />
      ))}
    </div>
  );
}

export default ReviewList;
