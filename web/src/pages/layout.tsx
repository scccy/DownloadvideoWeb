import React from 'react';
import { useLocation, useNavigate, useOutlet } from 'react-router-dom';
import { MenuFoldOutlined, MenuUnfoldOutlined } from '@ant-design/icons';
import { Layout as AntdLayout, Button, Menu, MenuProps, theme } from 'antd';
import { KeepAlive } from '../components';

const { Header, Sider, Content } = AntdLayout;

const Layout: React.FC = () => {
  const [collapsed, setCollapsed] = React.useState(false);
  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();
  const nav = useNavigate();
  const location = useLocation();
  const outlet = useOutlet();

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

  console.log(outlet);

  return (
    <AntdLayout style={{ height: '100vh' }}>
      <Sider trigger={null} collapsible collapsed={collapsed}>
        <div className="demo-logo-vertical" />
        <Menu
          theme="dark"
          mode="inline"
          selectedKeys={location.pathname.split('/')}
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
          <KeepAlive>{outlet?.props.children.props.children}</KeepAlive>
        </Content>
      </AntdLayout>
    </AntdLayout>
  );
};

export default Layout;
