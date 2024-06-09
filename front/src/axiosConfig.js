// src/axiosConfig.js
import axios from 'axios';

const instance = axios.create({
    baseURL: 'https://nysams.com', // 여기에 Django 서버의 URL을 설정합니다.
    // baseURL: 'http://192.0.0.2:8000', // 여기에 Django 서버의 URL을 설정합니다.
});

export default instance;
