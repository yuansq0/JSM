const express = require('express');
const app = express();
app.use(express.json());

// 模拟的用户数据
const users = {
    sqy: 'qq', // 用户名: 密码
};

// 登录 API
app.post('/api/login', (req, res) => {
    const { username, password } = req.body;

    if (users[username] && users[username] === password) {
        res.json({ success: true });
    } else {
        res.json({ success: false });
    }
});

// 启动服务器
app.listen(3000, () => {
    console.log('服务器运行在 http://localhost:3000');
});
