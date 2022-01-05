function ReviewForm({ handleChange, handleSubmit }) {
  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSubmit();
    }
  };

  return (
    <div>
      <form>
        <div class="rounded border-2 border-gray-300 p-3 my-3">
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2">
              평점
            </label>

            <select
              onChange={handleChange}
              name="heart"
              class="block appearance-none w-full bg-white border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
            >
              <option>0점</option>
              <option>1점</option>
              <option>2점</option>
              <option>3점</option>
              <option>4점</option>
              <option>5점</option>
            </select>
            <label class="block text-gray-700 text-sm font-bold mb-2">
              리뷰
            </label>
            <textarea
              className="shadow appearance-none border border-gray-500 rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
              onChange={handleChange}
              onKeyPress={handleKeyPress}
              name="content"
            />

            <button
              className="shadow border bg-blue-100 hover:bg-blue-300 border-blue-500 rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight"
              onClick={handleSubmit}
            >
              저장하기
            </button>
          </div>
        </div>
      </form>
    </div>
  );
}

export default ReviewForm;
