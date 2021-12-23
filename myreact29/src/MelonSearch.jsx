import { useState } from 'react';
import { Input } from 'antd';

function MelonSearch() {
  const [query, setQuery] = useState('');

  const handleChange = (e) => {
    const {
      target: { value },
    } = e;
    console.group('handleChange');
    console.log(value);
    console.groupEnd();
    setQuery(value);
  };
  const handlePressEnter = () => {
    console.group('handlePressEnter');
    console.log('검색어 ${query}(으)로 검색합니다.');
    console.groupEnd();
  };

  return (
    <div style={{ width: 300, margin: '0 auto' }}>
      <h2>멜론 검색</h2>
      검색어: {query}
      <Input
        placeholder="검색어를 입력해주세요."
        onChange={handleChange}
        onPressEnter={handlePressEnter}
      />
    </div>
  );
}

export default MelonSearch;
