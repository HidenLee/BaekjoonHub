def solution(game_board, table):
    N = len(table)
    blocks = []
    delta = [(1,0),(0,1),(-1,0),(0,-1)]
    for i in range(N):
        for j in range(N):
            if not table[i][j]:
                continue
            block = set([(0,0)])
            stack = [(i,j)]
            while stack:
                oy,ox = stack.pop()
                for ny,nx in [(oy+dy,ox+dx) for dy,dx in delta if 0<=ox+dx<N and 0<=oy+dy<N and table[oy+dy][ox+dx]]:
                    if (i-ny,j-nx) not in block:
                        block.add((i-ny,j-nx))
                        stack.append((ny,nx))
            for by,bx in block:
                table[i-by][j-bx] = 0
            blocks.append(block)

    answer = 0
    block_visit = [False for _ in range(len(blocks))]
    for i in range(N):
        for j in range(N):
            if game_board[i][j]:
                continue
            blank = set([(0,0)])
            stack = [(i,j)]
            while stack:
                oy,ox = stack.pop()
                for ny,nx in [(oy+dy,ox+dx) for dy,dx in delta if 0<=ox+dx<N and 0<=oy+dy<N and not game_board[oy+dy][ox+dx]]:
                    if (i-ny,j-nx) not in blank:
                        blank.add((i-ny,j-nx))
                        stack.append((ny,nx))
            flag = False
            for idx,block in enumerate(blocks):
                if block_visit[idx]:
                    continue
                if len(blank) != len(block):
                    continue
                block_copy = list(block)
                for _ in range(4):
                    block_copy = [(by,-bx) for bx,by in block_copy]
                    if all([True if 0<=by+j<N and 0<=bx+i<N and game_board[bx+i][by+j] == 0 else False for bx,by in block_copy]):
                        flag = True
                        for bx,by in block_copy:
                            game_board[bx+i][by+j] = 1
                        break
                if flag:
                    block_visit[idx] = True
                    answer+=len(block_copy)
                    
                    break
                    
                    
                    
            
    
            
    return answer