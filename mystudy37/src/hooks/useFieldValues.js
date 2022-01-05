import { useState } from 'react';

function useFieldValues() {
  const [fieldValues, setFieldValues] = useState({});

  const handleChange = (e) => {
    const { name, value } = e.target;

    setFieldValues({
      ...fieldValues,
      [name]: value,
    });
  };

  return [fieldValues, handleChange];
}

export default useFieldValues;
