within DymolaExamples.Examples_Filters;
model Test_Model_Filters_ModelSwitching
  parameter Real y_start=0;
  Modelica.Blocks.Sources.Pulse InputSignal(
    startTime=0.1,
    period=2,
    offset=0.1);
      Chebyshev_fmu UUT( y_start=y_start);
equation

  connect(InputSignal.y, UUT.u1);
end Test_Model_Filters_ModelSwitching;
