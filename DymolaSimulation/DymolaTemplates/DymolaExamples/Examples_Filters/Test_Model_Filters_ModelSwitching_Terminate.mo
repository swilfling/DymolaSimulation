within DymolaExamples.Examples_Filters;
model Test_Model_Filters_ModelSwitching_Terminate
  parameter Real fmi_NumberOfSteps = 1000;
  parameter Real fmi_StartTime=0;
  parameter Real fmi_StopTime=10;
  parameter Real y_start=0;
  Modelica.Blocks.Sources.Step InputSignal(
    startTime=0.1,
    height=1,
    offset=0);
  Modelica.Blocks.Math.Feedback error_calc;
  TestbenchComponents.Threshold_Terminator threshold_Terminator(threshold=
       0.1);
      Chebyshev_fmu UUT(y_start=y_start, fmi_NumberOfSteps=fmi_NumberOfSteps,
    fmi_StartTime=fmi_StartTime, fmi_StopTime=fmi_StopTime);
equation

  connect(InputSignal.y, UUT.u1);
  connect(UUT.y1, error_calc.u1);
  connect(error_calc.u2, UUT.u1);
  connect(error_calc.y, threshold_Terminator.u1);
end Test_Model_Filters_ModelSwitching_Terminate;
