def solution(record):
    
    seq, uids = 0, dict()
    log = []
    for rec in record:
        r = rec.split()
        if r[0] == 'Enter':
            uids[r[1]] = r[2]
            log.append(r[1] + "님이 들어왔습니다.")
        elif r[0] == 'Leave':
            log.append(r[1] + "님이 나갔습니다.")
        else :
            uids[r[1]] = r[2]

    for i,l in enumerate(log):
        uid = l.split('님이')[0]

        log[i] = l.replace(uid, uids[uid])
        
    
    return log