dino_main:训练代码可参考此code

多模态相关：
1.可用数据集 vlm_data, 博客 vlm_data_blog
2.wukong 数据集相关

多模态代码：
1.Qwen2-VL-main.zip  千问多模态模型
2.WePOINTS-main.zip  微信多模态模型，可参考测试流程
  We use VLMEvalKit to evaluate the performance of our models. Please follow the installation instructions to install the toolkit.
  Then, you can evaluate POINTS using the following command:

  # before running the evaluation below, please enter the root directory of VLMEvalKit
  torchrun --nproc-per-node=8 --master_port=8888 --no-python python run.py --data MMMU_DEV_VAL MMBench_DEV_EN MMBench_TEST_EN_V11 MMBench_TEST_CN_V11       HallusionBench OCRBench AI2D_TEST MMStar MMVet MathVista_MINI MME RealWorldQA LLaVABench POPE  --model POINTS-Yi-1.5-9B-Chat --verbose --work-dir ./


