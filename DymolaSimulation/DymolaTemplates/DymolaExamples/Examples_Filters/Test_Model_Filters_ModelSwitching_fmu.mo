within DymolaExamples.Examples_Filters;
model Test_Model_Filters_ModelSwitching_fmu
  parameter Real y_start=0;
  parameter Real fmi_NumberOfSteps = 1000;
  parameter Real fmi_StartTime=0;
  parameter Real fmi_StopTime=10;
  Modelica.Blocks.Sources.Pulse InputSignal(
    startTime=0.1,
    period=2,
    offset=0.1);
equation
Chebyshev_fmu UUT(y_start=y_start)                       annotation (Placement(transformation(extent={{22,10},
            {42,30}})));
  connect(InputSignal.y, UUT.u1);
end Test_Model_Filters_ModelSwitching_fmu;
