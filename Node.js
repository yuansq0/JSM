const express = require('express');
const cors = require('cors');
const app = express();

// 中间件
app.use(cors());
app.use(express.json());

// 模拟的用户数据（实际应用中应存储在数据库中，并加密密码）
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
    console.log('服务器已启动，访问 http://localhost:3000');
});
