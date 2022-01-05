import useFieldValues from 'hooks/useFieldValues';
import { useState } from 'react';
import Todo from './Todo';
import TodoForm from './TodoForm';
import './TodoList.css';

const INITIAL_STATE = [
  { content: '장고 업글하기', color: 'Coral' },
  { content: '파이썬 익히기', color: 'Brown' },
  { content: '리액트 익히기', color: 'Brown' },
];

function TodoList() {
  const [todoList, setTodoList] = useState(INITIAL_STATE);
  const [fieldValues, handleChange, clearFieldValues] = useFieldValues({
    content: '',
    color: 'Coral',
  });

  const removeTodo = (todoIndex) => {
    setTodoList((prevTodoList) =>
      prevTodoList.filter((_, index) => index !== todoIndex),
    );
  };
  const appendTodo = () => {
    console.log('새로운 todo추가');

    const todo = { ...fieldValues };

    //setter에 값 함수 지정 방식

    setTodoList((prevTodoList) => [...prevTodoList, todo]);

    clearFieldValues();
  };

  return (
    <div className="todo-list">
      <h2>Todo List</h2>

      <TodoForm
        fieldValues={fieldValues}
        handleChange={handleChange}
        handleSubmit={appendTodo}
      />
      <hr />
      {JSON.stringify(fieldValues)}

      <button
        className="bg-red-500 text-gray-100 cursor-pointer"
        onClick={() => clearFieldValues()}
      >
        clear
      </button>

      {/* 
      <input
        type="text"
        value={inputText}
        onChange={changedInputText}
        onKeyPress={appendInputText}
      /> */}

      {todoList.map((todo, index) => (
        <Todo todo={todo} onClick={() => removeTodo(index)} />
      ))}
    </div>
  );
}

export default TodoList;
