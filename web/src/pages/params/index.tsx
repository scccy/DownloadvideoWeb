import { Form, FormProps, Input } from 'antd';
import React from 'react';
import { useParams } from '../../store/params';

const Params: React.FC = () => {
  const formData = useParams();
  const handleFormChange: FormProps['onValuesChange'] = (
    changeValues,
    values,
  ) => {
    formData.setParams(changeValues);
  };

  return (
    <Form
      initialValues={formData}
      layout="vertical"
      style={{ maxWidth: '600px' }}
      onValuesChange={handleFormChange}
    >
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
