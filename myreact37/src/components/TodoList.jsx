import { useState } from 'react';
import Todo from './Todo';
import './TodoList.css';
import TodoForm from './TodoForm';
import useFieldValues from 'hooks/useFieldValues';

const INITIAL_STATE = [
  { content: '장고 업글하기' },
  { content: '파이썬 익히기' },
  { content: '리액트 익히기' },
];

function TodoList() {
  const [todoList, setTodoList] = useState(INITIAL_STATE);
  const [fieldValues, handleChange] = useFieldValues();

  const removeTodo = (todoIndex) => {
    setTodoList((prevTodoList) =>
      prevTodoList.filter((_, index) => index !== todoIndex),
    );
  };

  //   const changedInputText = (e) => {
  //     setInputText(e.target.value);
  //   };
  //   const appendInputText = (e) => {
  //     console.log('e.key :', e.key);
  //     if (e.key === 'Enter') {
  //       // todolist배열 끝에 inputText를 추가합니다.
  //       // input text를 다시 비웁니다. => input박스 ui가 비워보이진 않음,
  //       console.log('inputText:', inputText);

  //       //setTodoList에 함수를 넘기는것
  //       //todolist 상탯값을 변경하는 것은 아님.(배열의 push를 사용x)

  //       setTodoList((prevTodoList) => {
  //         return [...prevTodoList, { content: inputText }];
  //       });
  //       setInputText('');
  //     }
  //   };

  return (
    <div className="todo-list">
      <h2>Todo List</h2>

      <TodoForm handleChange={handleChange} />
      <hr />
      {JSON.stringify(fieldValues)}
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
