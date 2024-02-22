import { useContext } from 'react';
import { ApiContext } from '../api/instance';

const useApi = () => {
  return useContext(ApiContext);
};

export { useApi };
