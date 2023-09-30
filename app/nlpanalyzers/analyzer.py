from abc import ABC, abstractmethod


class NlpAnalyzer(ABC):

    @abstractmethod
    def analyzeStatement(
        self,
        statement,
    ):
        pass
