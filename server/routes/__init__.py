from flask import Blueprint, abort
from functools import wraps


routes = Blueprint('routes', __name__)


from .employeeRouter import *
from .levelRouter import *
from .specializationRouter import *
from .loginRouter import *
from .cabinetRouter import *
from .patientRouter import *
from .timetableRouter import *
from .appointmentRouter import *
from .docotorVisitRouter import *
from .referralRouter import *
from .labResultRouter import *



