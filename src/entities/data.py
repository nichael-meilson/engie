'''
Michael Neilson <github: nichael-meilson>
2023-01-25
'''
import abc

import pydantic


class Data(pydantic.BaseModel, abc.ABC):
    def w(self, **attributes):
        return self.copy(update=attributes)