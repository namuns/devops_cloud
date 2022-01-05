import { useState } from 'react';

const INITIAL_STATE = [
  { content: '장고 업글하기' },
  { content: '파이썬 업글하기' },
  { content: '리액트 업글하기' },
];

function TodoList() {
  const [inputText, setInputText] = useState('');
  const [todoList, setTodoList] = useState(INITIAL_STATE);

  const removeTodo = (todoIndex) => {
    setTodoList((prevTodoList) =>
      prevTodoList.filter((_, index) => index !== todoIndex),
    );
  };

  const changedInputText = (e) => {
    setInputText(e.target.value);
  };

  const appendInputText = (e) => {
    if (e.key === 'Enter') {
      setTodoList((prevTodoList) => {
        return [...prevTodoList, { content: inputText }];
      });
      setInputText('');
    }
  };

  return (
    <div>
      <h2>Todo List</h2>

      <input
        type="text"
        value={inputText}
        onChange={changedInputText}
        onKeyPress={appendInputText}
      />

      {todoList.map((todo, index) => (
        <div onClick={() => removeTodo(index)}>{todo.content}</div>
      ))}
    </div>
  );
}

export default TodoList;
