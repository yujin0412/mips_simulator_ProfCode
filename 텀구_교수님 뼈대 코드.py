# 필요 함수들
    # 시뮬레이터 명령어 처리 함수(기존 명령어 해석 함수 사용)
    # 메모리 접근 함수 -> unsigned int MEM(unsigned int A, int V, int nRW, int S)
    # 레지스터 접근 함수 -> unsigned int REG(unsigned int A,, unsigned int V, unsigned int nRW)
    # ALU 함수 및 관련 함수 -> int ALU(int X, int Y, int C, int *Z)
    # PC 갱신 함수


unsigned int PC, IR;
void main(){
    while(1){
        #Get Command Line
        switch(opcode){
            case 'l':   #l<실행 파일 이름>
                # 실행 파일이 시뮬레이터의 메모리에 올라감
                ## 실행 파일은 바이너리 파일로 구성
                ## 프로그램은 프로그램 메모리 0x400000번지부터 로드된다고 가정

            case 'j':   #j<프로그램 시작 위치>
                # 입력한 위치에 시뮬레이터 실행 준비
                ## PC를 특정한 주소 값으로 설정하여 그 주소부터 실행할 수 있게 함

            case 'g':
                # 현재 PC위치에서 시뮬레이터가 명령어를 끝까지 처리
                ## 프로그램의 끝은 syscall 10 명령어라 가정
                ## syscal 10 명령어를 만나면 -> 사용자 명령을 받는 상태로 중지
                
            case 'sr':  #sr<register number> <value>>
                # 특정 레지스터의 값 설정
            case 'sm':  #sm <location> <value>
                # 메모리 특정 주소의 값 설정

            case 'm':   #m <start> <end>
                # start~end 범위의 메모리 내용 출력

            case 'r':
                # 현재 레지스터 내용 출력

            case 'x':
                # 시뮬레이터 프로그램의 종료

            case 'help':
                # 사용할 수 있는 명령어 안내

            case 'break':
                # 중간 break point에서 중지
                ## 'g' 구현 방법 참고
            
        }
    }
}

void showRegister(void){
    int i;
    cout << "[REGISTER]" << endl;
    for(i=0; i<REG_SIZE, i++){
        cout << "R" << i << "=";
        cout << R[i] << endl;
    }
    cout << "PC" << PC << endl;
}

void setPC(unsigned int val){
    PC = val;
    return;
}