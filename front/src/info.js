import React from 'react';
import './styles.css';

function Info() {
    return (
        <div>
            <h2>1. 홈페이지 접속</h2>
            <p>아래 링크를 클릭하여 홈페이지에 접속하세요.</p>
            <a href="https://map.kakao.com/" target="_blank" rel="noopener noreferrer" className="button">카카오맵 접속하기</a>
            <img src={require('./image/1.png')} alt="불러오기 오류" className="guide-image" />
            <h2>2. 검색창에 식당 이름 입력 및 새창 접속하기</h2>
            <p>아래 사진과 같이 순서에 맞게 진행하세요.</p>
            <ol>
                <li>검색창에 검색하고자 하는 식당 이름을 입력합니다.</li>
                <li>지도에 식당 창이 뜨면 식당 이름을 클릭해 새창에 접속합니다.</li>
            </ol>
            <img src={require('./image/2.png')} alt="불러오기 오류" className="guide-image" />
            <img src={require('./image/3.png')} alt="불러오기 오류" className="guide-image" />
            <h2>3. 검색창 URL 확인</h2>
            <p>URL에서 https://map.kakao.com/ 뒤에 붙은 숫자를 확인하세요.</p>
            <ol>
                <li>URL에서 특정 번호를 확인 후 복사해줍니다.</li>
                <li>해당 번호를 어플 검색창에 입력하면 감성분석 리뷰를 확인할 수 있습니다.</li>
            </ol>
            <img src={require('./image/4.png')} alt="불러오기 오류" className="guide-image" />
            <img src={require('./image/5.png')} alt="불러오기 오류" className="guide-image" />
        </div>
    );
}

export default Info;
