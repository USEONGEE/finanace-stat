// src/axiosConfig.js
import axios from 'axios';

const instance = axios.create({
    baseURL: 'http://localhost:8000', // 여기에 Django 서버의 URL을 설정합니다.
});

export default instance;
