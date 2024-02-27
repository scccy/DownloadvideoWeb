import { Form, FormProps, Input } from 'antd';
import React from 'react';
import { useParams } from '../../store';
import styles from './index..module.scss';

const Params: React.FC = () => {
  const params = useParams();

  const handleValueChange: FormProps['onValuesChange'] = (
    valueChanges,
    value,
  ) => {
    params.setParams(value);
  };

  return (
    <Form
      layout="vertical"
      initialValues={params}
      className={styles.container}
      onValuesChange={handleValueChange}
    >
      <Form.Item name="cookie" label="抖音网页版 Cookie">
        <Input.TextArea
          className={styles.cookie}
          name="cookie"
          placeholder="抖音网页版 Cookie, 必需参数; 建议通过程序写入配置文件，亦可手动编辑"
        />
      </Form.Item>
    </Form>
  );
};

export default Params;
