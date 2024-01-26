a = "wWkIfZirBvirHPunlMBRmtKUScoesPsBAGAYungWgrbhzBtyRQANHMKowHaoZuCyLiXjakLLzHqrKLbRHaYZcAbafzUaBZSyCYVmWppWJspfSRUitYnKGySDGrBJBCYELZkuIyujtNtHlBlaFCIKBiXnVpOUTKZOhwvOFxKfdvWfIHXEuQcQujhmlrefumHCQlbJiQMSoznsCarHiKNCDBFDdROdbhdQQfJRstdmlkIPRsrTNkNUThjFKvtsJOeZHIlktuZVKNkmooruEAZLVEMGlfKeabrWMmkcIJmdhhrifFPLQmugNYtMqDGpbzodXuXnTRFguBEZZhnulHGFvpPwVXLYofeFDRUXeyNCbuZFqjCQdSAZheHXTMZhPcDNTWiQBKdakUQcOKDjaFqpSelJYrLxayNdmovXtnrPQodHEdMDmqszStzsizksSEZJtvmWjWAoKemgiruZlYWEUUBLKIlspEbIpwjRbPZzAmqCNbsUsicAuvMIjgDzEjvCnVhsknaMWbpzSEQvNYPbVzfupZKwdjftgtzoDieJGHSXTQHwPpxWvofuqvDsrwHpTIbHAwcxJuHGzkRZtJeqstAIdvOYFSmYaiEqqWcvxsEdnevLiiZPfSyASdOIeQDMBGFCfjUCmyavFWLgTWIzPAizASHoqktYbDelxQtSKHvusnMAlQqTBxtGhcpLSvUhKbbJoWyljZOgwEBWQHjOUNwJPEqSeNNIGeNwNcPCDmzGzTQnaabmiPEJZBhpNhWWddXvZnsuLZPNdjpnMMTDFXnYMlmqRbxfWILmfdAbUdoTlETADabIaNCZwHLMjkiARFOXqMxmSeuXdWIQrfxBPhNVzRmVjVXOyoSkgGsssWDaB" 
b= "hZQQVXCVUtvzMNCfApArBJTGwxGVKNQzmttmjgcGbxveszTCEJRZFeoJPLctNKfnITVckSvkdQeVuPaPNHqBDCMcrSjmrKnlhgucDjbhKBJmLyjmrZgPDdwxInCBpEFlfWksOBtQGRQhtnHOQCDdbNVBjzDivnEEkJBROsGQnBAWoIfTqdmEAZyWESjsLUpRMjcBHHFcBUALXxYRVBEnwPotMOLBpJnHgbXHQVvqMCYHqldzXrXVkEiZUuaQqAKcfaJuDjAlCIMllIloPqoSDbjVmtBZudpbWfegHiHZcLKFNnrIwpvjgPxISlUTDiTXRyauyklyCINESPYZvOUuFbYHEZkUhbUArWaxVVqDfITEpZJylYvvHRltAwOxsFdKmojVrCfJqbYkxIltNahwwLnlUlgXTZAKSJXIwIxfgtFeovrBDBWYIuxHTPTxFWPJPXXxOYjUBbXTuEGJupviMkJvGfMqlSEogzDunKEKNMvmZxOLewJiFVyehafCCXCytTHIRtJcLurzpFGCFpsuFXLhjsJDKnGPzjXtRtXYjVSiMGvTSFRMdWbiKpLxCbPzdjPAbUJESeHJWlvdpGITPazfVQuCYVnAaiBOtsdAAqaSFRhAVTBLkfOJMJVpLrBwnEBTLZhpMtxtwyFCvozdgNgjISsAOregSdkJiCpicQYLNCkOfLmWmJvrHWngoyZQhzWAgZuNhwXfdbCniKHaogpHrUkJwhkSwphFoKEyHlvuQApyqltoaxvzmBCsKYsMHknunmYfYrKjYIjbtwvfdTsERKcnHuHDkMfZHitLCHwIzDjFkpXmmCpIWjHTrKHdrQQsspqHMOKJZZskUsBYmFyBLUDjGEovwzWETUfOyEtLo"
#Back-end complete function Template for Python 3
from collections import Counter

class Solution:
    def transform(self, A, B): 
        n=len(A)
        if Counter(A)!=Counter(B): return -1
        i=j=n-1
        while i>=0:
            if A[i]==B[j]:
                i-=1
                j-=1
            else:
                i-=1
        return j-i



#Back-end complete function Template for Python 3

class Solution:
    def transform(self, A, B): 
        #code here.
        d = dict()
        for c in A:
            d[c] = d.get(c,0) + 1
        for c in B:
            d[c] = d.get(c,0) - 1
        if any(d.values()):
            return -1
        j = len(B) - 1
        for c in A[::-1]:
            if B[j] == c:
                j -= 1
        return j + 1        



