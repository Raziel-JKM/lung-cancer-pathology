# 2022 암 예후예측 데이터 구축 AI 경진대회
## 폐암 병리 슬라이드 이미지 세그멘테이션

### 코드 구조
- USER 경로에서 코드 개발 필요
```
$/
├── DATA/
│   ├── train
│   │   ├── x
│   │   └── y
│   ├── test
│   │   └── x
│   └── sample_submission.zip
└── USER/baseline
    ├── config
    │   ├── predict.yaml
    │   ├── train.yaml
    │   └── preprocess.yaml
    ├── models/
    │   └── utils.py
    ├── modules/
    │   ├── datasets.py
    │   ├── earlystoppers.py
    │   ├── losses.py
    │   ├── metrics.py
    │   ├── optimizers.py
    │   ├── recorders.py
    │   ├── scalers.py
    │   ├── schedulers.py
    │   ├── trainer.py
    │   └── utils.py
    ├── readme.md
    ├── predict.py
    ├── preprocess.py
    └── train.py
```

- config : 학습/추론에 필요한 파라미터 등을 기록하는 yml 파일
- models  
    - utils.py : config에서 지정한 모델 클래스를 리턴
- modules
    - datasets.py : dataset 클래스
    - earlystopper.py : loss가 특정 에폭 이상 개선되지 않을 경우 멈춤
    - losses.py : config에서 지정한 loss function을 리턴
    - metrics.py : config에서 지정한 metric을 리턴
    - optimizers.py : config에서 지정한 optimizer를 리턴
    - recorders.py : log, learning curve 등을 기록
    - schedulers.py : learning rate 스케쥴링
    - scalers.py : normalized 된 이미지를 리턴
    - trainer.py : 에폭 별로 수행할 학습 과정
    - utils.py : 여러 확장자 파일을 불러오거나 여러 확장자로 저장하는 등의 함수
- train.py : 학습 시 실행하는 코드, config/train.yaml에서 관련 Argument 조정
- predict.py : 추론 시 실행하는 코드, config/predict.yaml에서 관련 Argument 조정
- preprocess.py : 원본 이미지를 resize 하여 저장, config/preprocess.yaml에서 관련 Argument 조정

### 사용 모델
- model : Unet

### 학습

1. `/USER/config/train.yaml` 수정
    1. DIRECTORY/dataset : 데이터 경로 지정(사진이 위치한 디렉토리)
    2. 이외 파라미터 조정
2. `/USER/results/train/` 내에 결과(weight, log, plot 등)가 저장됨


### 추론

1. `/USER/config/predict.yaml` 수정
    1. DIRECTORY/dataset : 데이터 경로 지정 (테스트 이미지가 위치한 디렉토리)
    2. TRAIN/train_serial : weight를 불러올 train serial (/USER/results/train 내 폴더명)지정
2. `/USER/results/predict/` 내에 결과(weight,log,mask 등)가 저장됨
