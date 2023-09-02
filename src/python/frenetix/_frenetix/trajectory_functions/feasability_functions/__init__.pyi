from __future__ import annotations
import frenetix._frenetix.trajectory_functions.feasability_functions
import typing
import frenetix._frenetix.trajectory_functions
import frenetix._frenetix

__all__ = [
    "CheckAccelerationConstraint",
    "CheckCurvatureConstraint",
    "CheckCurvatureRateConstraint",
    "CheckVelocityConstraint",
    "CheckYawRateConstraint"
]


class CheckAccelerationConstraint(frenetix._frenetix.trajectory_functions.FeasabilityStrategy, frenetix._frenetix.trajectory_functions.TrajectoryStrategy):
    def __init__(self, switchingVelocity: float, maxAcceleration: float) -> None: ...
    def evaluate_trajectory(self, trajectory: frenetix._frenetix.TrajectorySample) -> None: ...
    pass
class CheckCurvatureConstraint(frenetix._frenetix.trajectory_functions.FeasabilityStrategy, frenetix._frenetix.trajectory_functions.TrajectoryStrategy):
    def __init__(self, deltaMax: float, wheelbase: float) -> None: ...
    def evaluate_trajectory(self, trajectory: frenetix._frenetix.TrajectorySample) -> None: ...
    pass
class CheckCurvatureRateConstraint(frenetix._frenetix.trajectory_functions.FeasabilityStrategy, frenetix._frenetix.trajectory_functions.TrajectoryStrategy):
    def __init__(self, wheelbase: float, velocityDeltaMax: float) -> None: ...
    def evaluate_trajectory(self, trajectory: frenetix._frenetix.TrajectorySample) -> None: ...
    pass
class CheckVelocityConstraint(frenetix._frenetix.trajectory_functions.FeasabilityStrategy, frenetix._frenetix.trajectory_functions.TrajectoryStrategy):
    def __init__(self) -> None: ...
    def evaluate_trajectory(self, trajectory: frenetix._frenetix.TrajectorySample) -> None: ...
    pass
class CheckYawRateConstraint(frenetix._frenetix.trajectory_functions.FeasabilityStrategy, frenetix._frenetix.trajectory_functions.TrajectoryStrategy):
    def __init__(self, deltaMax: float, wheelbase: float) -> None: ...
    def evaluate_trajectory(self, trajectory: frenetix._frenetix.TrajectorySample) -> None: ...
    pass
