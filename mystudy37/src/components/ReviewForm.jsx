function ReviewForm({ fieldValues, handleChange, handleSubmit }) {
  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSubmit();
    }
  };

  return (
    <div className="border-2 border-red-500 p-3">
      <h2 className="text-lg underline">ReviewForm</h2>

      <select onChange={handleChange} name="color" value={fieldValues.color}>
        <option>blue</option>
        <option>red</option>
      </select>

      <input
        type="text"
        className="border-2 border-gray-200"
        onChange={handleChange}
        onKeyPress={handleKeyPress}
        name="content"
        value={fieldValues.content}
      />

      <button onClick={() => handleSubmit()}>저장</button>
    </div>
  );
}

export default ReviewForm;
