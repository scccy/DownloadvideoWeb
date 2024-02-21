import { Form, Input } from 'antd';
import React from 'react';

const Params: React.FC = () => {
  return (
    <Form layout="vertical" style={{ maxWidth: '600px' }}>
      <Form.Item label="keyword" name="keyword">
        <Input />
      </Form.Item>

      <Form.Item label="type" name="type">
        <Input />
      </Form.Item>

      <Form.Item label="pages" name="pages">
        <Input />
      </Form.Item>

      <Form.Item label="sort_type" name="sort_type">
        <Input />
      </Form.Item>

      <Form.Item label="publish_time" name="publish_time">
        <Input />
      </Form.Item>
    </Form>
  );
};

export default Params;
