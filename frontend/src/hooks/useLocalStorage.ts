import { useEffect, useState } from "react";

function getSavedValue(key: string, initialValue: any) {
  const savedValue = JSON.parse(
    localStorage.getItem(key) || JSON.stringify(initialValue)
  );

  if (savedValue) return savedValue;

  return initialValue;
}

const useLocalStorage = (key: string, initialValue: any) => {
  const [value, setValue] = useState(getSavedValue(key, initialValue));

  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(value));
  }, [value, key]);

  return [value, setValue];
};

export default useLocalStorage;
