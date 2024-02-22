import React from 'react';
import { Outlet, useNavigate } from 'react-router-dom';
import { Layout as AntdLayout, Button, Menu, MenuProps, theme } from 'antd';
import { MenuFoldOutlined, MenuUnfoldOutlined } from '@ant-design/icons';

const { Header, Sider, Content } = AntdLayout;

const Layout: React.FC = () => {
  const [collapsed, setCollapsed] = React.useState(false);
  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();
  const nav = useNavigate();

  const items: MenuProps['items'] = [
    {
      key: 'params',
      label: '参数',
    },
    {
      key: 'gather',
      label: '采集',
    },
    {
      key: 'download',
      label: '下载',
    },
    {
      key: 'process',
      label: '视频处理',
    },
  ];

  const handleMenuClick: MenuProps['onClick'] = event => {
    const { key } = event;
    nav(`./${key}`, { relative: 'path' });
  };

  return (
    <AntdLayout style={{ height: '100vh' }}>
      <Sider trigger={null} collapsible collapsed={collapsed}>
        <div className="demo-logo-vertical" />
        <Menu
          theme="dark"
          mode="inline"
          defaultSelectedKeys={[items[0]?.key!]}
          items={items}
          onClick={handleMenuClick}
        />
      </Sider>
      <AntdLayout>
        <Header style={{ padding: 0, background: colorBgContainer }}>
          <Button
            type="text"
            icon={collapsed ? <MenuUnfoldOutlined /> : <MenuFoldOutlined />}
            onClick={() => setCollapsed(!collapsed)}
            style={{
              fontSize: '16px',
              width: 64,
              height: 64,
            }}
          />
        </Header>
        <Content
          style={{
            margin: '24px 16px',
            padding: 24,
            minHeight: 280,
            overflowY: 'scroll',
            background: colorBgContainer,
            borderRadius: borderRadiusLG,
          }}
        >
          <Outlet />
        </Content>
      </AntdLayout>
    </AntdLayout>
  );
};

export default Layout;
